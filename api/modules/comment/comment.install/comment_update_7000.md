# comment_update_7000()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 108–136 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L108-L136)
- **Module/theme:** comment
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function comment_update_7000()
```

## Documentation

```text
Rename comment display setting variables.
```

## Code

```php
function comment_update_7000() {
  $types = _update_7000_node_get_types();
  foreach ($types as $type => $type_object) {
    variable_del('comment_default_order' . $type);

    // Drupal 6 had four display modes:
    // - COMMENT_MODE_FLAT_COLLAPSED = 1
    // - COMMENT_MODE_FLAT_EXPANDED = 2
    // - COMMENT_MODE_THREADED_COLLAPSED = 3
    // - COMMENT_MODE_THREADED_EXPANDED = 4
    //
    // Drupal 7 doesn't support collapsed/expanded modes anymore, so we
    // migrate all the flat modes to COMMENT_MODE_FLAT (0) and all the threaded
    // modes to COMMENT_MODE_THREADED (1).
    $setting = variable_get('comment_default_mode_' . $type, 4);
    if ($setting == 3 || $setting == 4) {
      variable_set('comment_default_mode_' . $type, 1);
    }
    else {
      variable_set('comment_default_mode_' . $type, 0);
    }

    // There were only two comment modes in the past:
    // - 1 was 'required' previously, convert into DRUPAL_REQUIRED (2).
    // - 0 was 'optional' previously, convert into DRUPAL_OPTIONAL (1).
    $preview = variable_get('comment_preview_' . $type, 1) ? 2 : 1;
    variable_set('comment_preview_' . $type, $preview);
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
