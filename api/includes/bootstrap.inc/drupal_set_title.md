# drupal_set_title()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 2221–2229 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L2221-L2229)

## Signature

```php
function drupal_set_title($title = NULL, $output = CHECK_PLAIN)
```

## Documentation

```text
Sets the title of the current page.

The title is displayed on the page and in the title bar.

@param $title
  Optional string value to assign to the page title; or if set to NULL
  (default), leaves the current title unchanged.
@param $output
  Optional flag - normally should be left as CHECK_PLAIN. Only set to
  PASS_THROUGH if you have already removed any possibly dangerous code
  from $title using a function like check_plain() or filter_xss(). With this
  flag the string will be passed through unchanged.

@return
  The updated title of the current page.
```

## Code

```php
function drupal_set_title($title = NULL, $output = CHECK_PLAIN) {
  $stored_title = &drupal_static(__FUNCTION__);

  if (isset($title)) {
    $stored_title = ($output == PASS_THROUGH) ? $title : check_plain($title);
  }

  return $stored_title;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
