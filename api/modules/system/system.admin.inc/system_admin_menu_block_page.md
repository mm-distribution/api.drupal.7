# system_admin_menu_block_page()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 66–75 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L66-L75)
- **Module/theme:** system

## Signature

```php
function system_admin_menu_block_page()
```

## Documentation

```text
Provide a single block from the administration menu as a page.

This function is often a destination for these blocks.
For example, 'admin/structure/types' needs to have a destination to be valid
in the Drupal menu system, but too much information there might be
hidden, so we supply the contents of the block.

@return
  The output HTML.
```

## Code

```php
function system_admin_menu_block_page() {
  $item = menu_get_item();
  if ($content = system_admin_menu_block($item)) {
    $output = theme('admin_block_content', array('content' => $content));
  }
  else {
    $output = t('You do not have any administrative items.');
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
