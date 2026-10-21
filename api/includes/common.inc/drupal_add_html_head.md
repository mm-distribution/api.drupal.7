# drupal_add_html_head()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 299–314 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L299-L314)

## Signature

```php
function drupal_add_html_head($data = NULL, $key = NULL)
```

## Documentation

```text
Adds output to the HEAD tag of the HTML page.

This function can be called as long as the headers aren't sent. Pass no
arguments (or NULL for both) to retrieve the currently stored elements.

@param $data
  A renderable array. If the '#type' key is not set then 'html_tag' will be
  added as the default '#type'.
@param $key
  A unique string key to allow implementations of hook_html_head_alter() to
  identify the element in $data. Required if $data is not NULL.

@return
  An array of all stored HEAD elements.

@see theme_html_tag()
```

## Code

```php
function drupal_add_html_head($data = NULL, $key = NULL) {
  $stored_head = &drupal_static(__FUNCTION__);

  if (!isset($stored_head)) {
    // Make sure the defaults, including Content-Type, come first.
    $stored_head = _drupal_default_html_head();
  }

  if (isset($data) && isset($key)) {
    if (!isset($data['#type'])) {
      $data['#type'] = 'html_tag';
    }
    $stored_head[$key] = $data;
  }
  return $stored_head;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
