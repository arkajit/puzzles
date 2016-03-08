An example ringpop application, taken from
https://ringpop.readthedocs.org/en/latest/programming_ringpop.html.

This application is a simple http server which routes requests
on `/objects/:id` to the appropriate node in the ring.

Usage
=====

1. Start the application: `node ringexample.js`
2. Lookup objects: `curl localhost:6000/objects/abc`
3. Try issuing `ringpop-admin` commands, e.g.
  `ringpop-admin status 127.0.0.1:3000`

  ADDRESS          STATUS   DAMPSCORE
 127.0.0.1:3000   alive    0..0
 127.0.0.1:3001   alive    0..0
 127.0.0.1:3002   alive    0..0

  `ringpop-admin leave 127.0.0.1:3000`
