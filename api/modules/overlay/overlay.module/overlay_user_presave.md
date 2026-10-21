# overlay_user_presave()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 122–126 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L122-L126)
- **Module/theme:** overlay
- **Implements:** [hook_user_presave()](../../user/user.api.php/hook_user_presave.md)

## Signature

```php
function overlay_user_presave(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_presave().
```

## Code

```php
function overlay_user_presave(&$edit, $account, $category) {
  if (isset($edit['overlay'])) {
    $edit['data']['overlay'] = $edit['overlay'];
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
