# system_check_http_request()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3443–3451 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3443-L3451)
- **Module/theme:** system

## Signature

```php
function system_check_http_request()
```

## Documentation

```text
Checks whether the server is capable of issuing HTTP requests.

The function sets the drupal_http_request_fail system variable to TRUE if
drupal_http_request() does not work and then the system status report page
will contain an error.

@return
 TRUE if this installation can issue HTTP requests.
```

## Code

```php
function system_check_http_request() {
  // Try to get the content of the front page via drupal_http_request().
  $result = drupal_http_request(url('', array('absolute' => TRUE)), array('max_redirects' => 0));
  // We only care that we get a http response - this means that Drupal
  // can make a http request.
  $works = isset($result->code) && ($result->code >= 100) && ($result->code < 600);
  variable_set('drupal_http_request_fails', !$works);
  return $works;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
