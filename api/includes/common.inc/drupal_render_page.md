# drupal_render_page()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6059–6087 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6059-L6087)

## Signature

```php
function drupal_render_page($page)
```

## Documentation

```text
Renders the page, including all theming.

@param $page
  A string or array representing the content of a page. The array consists of
  the following keys:
  - #type: Value is always 'page'. This pushes the theming through
    page.tpl.php (required).
  - #show_messages: Suppress drupal_get_message() items. Used by Batch
    API (optional).

@see hook_page_alter()
@see element_info()
```

## Code

```php
function drupal_render_page($page) {
  $main_content_display = &drupal_static('system_main_content_added', FALSE);

  // Allow menu callbacks to return strings or arbitrary arrays to render.
  // If the array returned is not of #type page directly, we need to fill
  // in the page with defaults.
  if (is_string($page) || (is_array($page) && (!isset($page['#type']) || ($page['#type'] != 'page')))) {
    drupal_set_page_content($page);
    $page = element_info('page');
  }

  // Modules can add elements to $page as needed in hook_page_build().
  foreach (module_implements('page_build') as $module) {
    $function = $module . '_page_build';
    $function($page);
  }
  // Modules alter the $page as needed. Blocks are populated into regions like
  // 'sidebar_first', 'footer', etc.
  drupal_alter('page', $page);

  // If no module has taken care of the main content, add it to the page now.
  // This allows the site to still be usable even if no modules that
  // control page regions (for example, the Block module) are enabled.
  if (!$main_content_display) {
    $page['content']['system_main'] = drupal_set_page_content();
  }

  return drupal_render($page);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
