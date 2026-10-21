# aggregator_admin_remove_feed_submit()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 238–241 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L238-L241)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_admin_remove_feed_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for aggregator_admin_remove_feed().

Removes all items from a feed and redirects to the overview page.
```

## Code

```php
function aggregator_admin_remove_feed_submit($form, &$form_state) {
  aggregator_remove($form_state['values']['feed']);
  $form_state['redirect'] = 'admin/config/services/aggregator';
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
