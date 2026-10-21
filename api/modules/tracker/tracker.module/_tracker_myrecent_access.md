# _tracker_myrecent_access()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 158–161 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L158-L161)
- **Module/theme:** tracker

## Signature

```php
function _tracker_myrecent_access($account)
```

## Documentation

```text
Access callback for tracker/%user_uid_optional.
```

## Code

```php
function _tracker_myrecent_access($account) {
  // This path is only allowed for authenticated users looking at their own content.
  return $account->uid && ($GLOBALS['user']->uid == $account->uid) && user_access('access content');
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
