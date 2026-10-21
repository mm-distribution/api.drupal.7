# drupal_set_page_content()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5786–5801 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5786-L5801)

## Signature

```php
function drupal_set_page_content($content = NULL)
```

## Documentation

```text
Sets the main page content value for later use.

Given the nature of the Drupal page handling, this will be called once with
a string or array. We store that and return it later as the block is being
displayed.

@param $content
  A string or renderable array representing the body of the page.

@return
  If called without $content, a renderable array representing the body of
  the page.
```

## Code

```php
function drupal_set_page_content($content = NULL) {
  $content_block = &drupal_static(__FUNCTION__, NULL);
  $main_content_display = &drupal_static('system_main_content_added', FALSE);

  if (!empty($content)) {
    $content_block = (is_array($content) ? $content : array('main' => array('#markup' => $content)));
  }
  else {
    // Indicate that the main content has been requested. We assume that
    // the module requesting the content will be adding it to the page.
    // A module can indicate that it does not handle the content by setting
    // the static variable back to FALSE after calling this function.
    $main_content_display = TRUE;
    return $content_block;
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
