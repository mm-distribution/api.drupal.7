# drupal_get_destination()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 525–544 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L525-L544)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function drupal_get_destination()
```

## Documentation

```text
Prepares a 'destination' URL query parameter for use with drupal_goto().

Used to direct the user back to the referring page after completing a form.
By default the current URL is returned. If a destination exists in the
previous request, that destination is returned. As such, a destination can
persist across multiple pages.

@return
  An associative array containing the key:
  - destination: The path provided via the destination query string or, if
    not available, the current path.

@see current_path()
@see drupal_goto()
```

## Code

```php
function drupal_get_destination() {
  $destination = &drupal_static(__FUNCTION__);

  if (isset($destination)) {
    return $destination;
  }

  if (isset($_GET['destination'])) {
    $destination = array('destination' => $_GET['destination']);
  }
  else {
    $path = $_GET['q'];
    $query = drupal_http_build_query(drupal_get_query_parameters());
    if ($query != '') {
      $path .= '?' . $query;
    }
    $destination = array('destination' => $path);
  }
  return $destination;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
