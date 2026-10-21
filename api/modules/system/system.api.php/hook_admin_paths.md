# hook_admin_paths()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 508–514 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L508-L514)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_admin_paths()
```

## Documentation

```text
Define administrative paths.

Modules may specify whether or not the paths they define in hook_menu() are
to be considered administrative. Other modules may use this information to
display those pages differently (e.g. in a modal overlay, or in a different
theme).

To change the administrative status of menu items defined in another module's
hook_menu(), modules should implement hook_admin_paths_alter().

@return
  An associative array. For each item, the key is the path in question, in
  a format acceptable to drupal_match_path(). The value for each item should
  be TRUE (for paths considered administrative) or FALSE (for non-
  administrative paths).

@see hook_menu()
@see drupal_match_path()
@see hook_admin_paths_alter()
```

## Code

```php
function hook_admin_paths() {
  $paths = array(
    'mymodule/*/add' => TRUE,
    'mymodule/*/edit' => TRUE,
  );
  return $paths;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_admin_paths()".

- [block_admin_paths()](../../block/block.module/block_admin_paths.md) — `modules/block/block.module`
- [book_admin_paths()](../../book/book.module/book_admin_paths.md) — `modules/book/book.module`
- [node_admin_paths()](../../node/node.module/node_admin_paths.md) — `modules/node/node.module`
- [openid_admin_paths()](../../openid/openid.module/openid_admin_paths.md) — `modules/openid/openid.module`
- [overlay_admin_paths()](../../overlay/overlay.module/overlay_admin_paths.md) — `modules/overlay/overlay.module`
- [shortcut_admin_paths()](../../shortcut/shortcut.module/shortcut_admin_paths.md) — `modules/shortcut/shortcut.module`
- [system_admin_paths()](../system.module/system_admin_paths.md) — `modules/system/system.module`
- [taxonomy_admin_paths()](../../taxonomy/taxonomy.module/taxonomy_admin_paths.md) — `modules/taxonomy/taxonomy.module`
- [translation_admin_paths()](../../translation/translation.module/translation_admin_paths.md) — `modules/translation/translation.module`
- [user_admin_paths()](../../user/user.module/user_admin_paths.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
