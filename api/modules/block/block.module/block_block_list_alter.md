# block_block_list_alter()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 764–846 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L764-L846)
- **Module/theme:** block
- **Implements:** [hook_block_list_alter()](../block.api.php/hook_block_list_alter.md)

## Signature

```php
function block_block_list_alter(&$blocks)
```

## Documentation

```text
Implements hook_block_list_alter().

Checks the page, user role, and user-specific visibility settings.
Removes the block if the visibility conditions are not met.
```

## Code

```php
function block_block_list_alter(&$blocks) {
  global $user, $theme_key;

  // Build an array of roles for each block.
  $block_roles = array();
  $result = db_query('SELECT module, delta, rid FROM {block_role}');
  foreach ($result as $record) {
    $block_roles[$record->module][$record->delta][] = $record->rid;
  }

  foreach ($blocks as $key => $block) {
    if (!isset($block->theme) || !isset($block->status) || $block->theme != $theme_key || $block->status != 1) {
      // This block was added by a contrib module, leave it in the list.
      continue;
    }

    // If a block has no roles associated, it is displayed for every role.
    // For blocks with roles associated, if none of the user's roles matches
    // the settings from this block, remove it from the block list.
    if (isset($block_roles[$block->module][$block->delta]) && !array_intersect($block_roles[$block->module][$block->delta], array_keys($user->roles))) {
      // No match.
      unset($blocks[$key]);
      continue;
    }

    // Use the user's block visibility setting, if necessary.
    if ($block->custom != BLOCK_CUSTOM_FIXED) {
      if ($user->uid && isset($user->data['block'][$block->module][$block->delta])) {
        $enabled = $user->data['block'][$block->module][$block->delta];
      }
      else {
        $enabled = ($block->custom == BLOCK_CUSTOM_ENABLED);
      }
    }
    else {
      $enabled = TRUE;
    }

    // Limited visibility blocks must list at least one page.
    if ($block->visibility == BLOCK_VISIBILITY_LISTED && empty($block->pages)) {
      $enabled = FALSE;
    }

    if (!$enabled) {
      unset($blocks[$key]);
      continue;
    }

    // Match path if necessary.
    if ($block->pages) {
      // Convert path to lowercase. This allows comparison of the same path
      // with different case. Ex: /Page, /page, /PAGE.
      $pages = drupal_strtolower($block->pages);
      if ($block->visibility < BLOCK_VISIBILITY_PHP) {
        // Convert the Drupal path to lowercase.
        $path = drupal_strtolower(drupal_get_path_alias($_GET['q']));
        // Compare the lowercase internal and lowercase path alias (if any).
        $page_match = drupal_match_path($path, $pages);
        if ($path != $_GET['q']) {
          $page_match = $page_match || drupal_match_path($_GET['q'], $pages);
        }
        // When $block->visibility has a value of 0
        // (BLOCK_VISIBILITY_NOTLISTED), the block is displayed on all pages
        // except those listed in $block->pages. When set to 1
        // (BLOCK_VISIBILITY_LISTED), it is displayed only on those pages
        // listed in $block->pages.
        $page_match = !($block->visibility xor $page_match);
      }
      elseif (module_exists('php')) {
        $page_match = php_eval($block->pages);
      }
      else {
        $page_match = FALSE;
      }
    }
    else {
      $page_match = TRUE;
    }
    if (!$page_match) {
      unset($blocks[$key]);
    }
  }
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
