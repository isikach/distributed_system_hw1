# Replicated log task
## Iteration 1

**Master** should expose a simple HTTP server (or alternative service with a similar API) with: 
+ POST method - appends a message into the in-memory list
+ GET method - returns all messages from the in-memory list

**Secondary** should expose a simple  HTTP server(or alternative service with a similar API)  with:
+ GET method - returns all replicated messages from the in-memory list
