# Establish DB connection ----
connectDB <- function(dblist, dbms = "MySQL", username = NULL, password = NULL, log_file, host = "localhost", port = 0) {
  
  if (dbms == "MySQL") {
    names <- dblist
  } else {
    names <- purrr::map(
      dblist,
      function(name) {
        name <- gsub(".*(?<=\\W)(\\w+)\\.db", "\\1", name, perl = T)
      }
    )
  }

  connections <- purrr::map(
    dblist,
    function(name) {
      tryCatch(
        {
          
          if (dbms == "MySQL") {
            conn <- DBI::dbConnect(
              RMariaDB::MariaDB(), 
              dbname = name,
              host = host,
              port = port,
              username = dbusername, 
              password = dbpassword
            )
          } else if (dbms == "SQLite") {
            conn <- RSQLite::dbConnect(
              RSQLite::SQLite(),
              name
            )
          }
          logMessage(
            paste("Connection established to database", name, "successfully."),
            log_file
          )
          return(conn)
        },
        error = function(cnd) {
          logMessage(
            paste("Failed to establish connection to database", name, "."),
            log_file
          )
          errorMessage(cnd, log_file)
        }
      )
    }
  )
  connections <- setNames(connections, names)
  return(connections)
}
