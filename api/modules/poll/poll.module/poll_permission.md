# poll_permission()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 70–84 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L70-L84)
- **Module/theme:** poll
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function poll_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function poll_permission() {
  $perms = array(
    'vote on polls' => array(
      'title' => t('Vote on polls'),
    ),
    'cancel own vote' => array(
      'title' => t('Cancel and change own votes'),
    ),
    'inspect all votes' => array(
      'title' => t('View details for all votes'),
    ),
  );

  return $perms;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
