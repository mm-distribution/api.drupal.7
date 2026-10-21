# aggregator_admin_remove_feed()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 217–231 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L217-L231)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_admin_remove_feed($form, $form_state, $feed)
```

## Documentation

```text
Deletes a feed.

@param $feed
  An associative array describing the feed to be cleared.

@see aggregator_admin_remove_feed_submit()
```

## Code

```php
function aggregator_admin_remove_feed($form, $form_state, $feed) {
  return confirm_form(
    array(
      'feed' => array(
        '#type' => 'value',
        '#value' => $feed,
      ),
    ),
    t('Are you sure you want to remove all items from the feed %feed?', array('%feed' => $feed->title)),
    'admin/config/services/aggregator',
    t('This action cannot be undone.'),
    t('Remove items'),
    t('Cancel')
  );
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
