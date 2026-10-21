# aggregator_categorize_items_submit()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 248–271 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L248-L271)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_categorize_items_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for aggregator_categorize_items().
```

## Code

```php
function aggregator_categorize_items_submit($form, &$form_state) {
  if (!empty($form_state['values']['categories'])) {
    foreach ($form_state['values']['categories'] as $iid => $selection) {
      db_delete('aggregator_category_item')
        ->condition('iid', $iid)
        ->execute();
      $insert = db_insert('aggregator_category_item')->fields(array('iid', 'cid'));
      $has_values = FALSE;
      foreach ($selection as $cid) {
        if ($cid && $iid) {
          $has_values = TRUE;
          $insert->values(array(
            'iid' => $iid,
            'cid' => $cid,
          ));
        }
      }
      if ($has_values) {
        $insert->execute();
      }
    }
  }
  drupal_set_message(t('The categories have been saved.'));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
