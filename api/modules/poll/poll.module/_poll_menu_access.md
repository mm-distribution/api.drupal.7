# _poll_menu_access()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 126–128 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L126-L128)
- **Module/theme:** poll

## Signature

```php
function _poll_menu_access($node, $perm, $inspect_allowvotes)
```

## Documentation

```text
Callback function to see if a node is acceptable for poll menu items.
```

## Code

```php
function _poll_menu_access($node, $perm, $inspect_allowvotes) {
  return user_access($perm) && ($node->type == 'poll') && ($node->allowvotes || !$inspect_allowvotes);
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
