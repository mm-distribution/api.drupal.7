# drupal_override_server_variables()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 628–654 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L628-L654)

## Signature

```php
function drupal_override_server_variables($variables = array())
```

## Documentation

```text
Sets appropriate server variables needed for command line scripts to work.

This function can be called by command line scripts before bootstrapping
Drupal, to ensure that the page loads with the desired server parameters.
This is because many parts of Drupal assume that they are running in a web
browser and therefore use information from the global PHP $_SERVER variable
that does not get set when Drupal is run from the command line.

In many cases, the default way in which this function populates the $_SERVER
variable is sufficient, and it can therefore be called without passing in
any input. However, command line scripts running on a multisite installation
(or on any installation that has settings.php stored somewhere other than
the sites/default folder) need to pass in the URL of the site to allow
Drupal to detect the correct location of the settings.php file. Passing in
the 'url' parameter is also required for functions like request_uri() to
return the expected values.

Most other parameters do not need to be passed in, but may be necessary in
some cases; for example, if Drupal's ip_address() function needs to return
anything but the standard localhost value ('127.0.0.1'), the command line
script should pass in the desired value via the 'REMOTE_ADDR' key.

@param $variables
  (optional) An associative array of variables within $_SERVER that should
  be replaced. If the special element 'url' is provided in this array, it
  will be used to populate some of the server defaults; it should be set to
  the URL of the current page request, excluding any $_GET request but
  including the script name (e.g., http://www.example.com/mysite/index.php).

@see conf_path()
@see request_uri()
@see ip_address()
```

## Code

```php
function drupal_override_server_variables($variables = array()) {
  // Allow the provided URL to override any existing values in $_SERVER.
  if (isset($variables['url'])) {
    $url = parse_url($variables['url']);
    if (isset($url['host'])) {
      $_SERVER['HTTP_HOST'] = $url['host'];
    }
    if (isset($url['path'])) {
      $_SERVER['SCRIPT_NAME'] = $url['path'];
    }
    unset($variables['url']);
  }
  // Define default values for $_SERVER keys. These will be used if $_SERVER
  // does not already define them and no other values are passed in to this
  // function.
  $defaults = array(
    'HTTP_HOST' => 'localhost',
    'SCRIPT_NAME' => NULL,
    'REMOTE_ADDR' => '127.0.0.1',
    'REQUEST_METHOD' => 'GET',
    'SERVER_NAME' => NULL,
    'SERVER_SOFTWARE' => NULL,
    'HTTP_USER_AGENT' => NULL,
  );
  // Replace elements of the $_SERVER array, as appropriate.
  $_SERVER = $variables + $_SERVER + $defaults;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
