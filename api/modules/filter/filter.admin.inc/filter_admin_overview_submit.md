# filter_admin_overview_submit()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 52–64 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L52-L64)
- **Module/theme:** filter

## Signature

```php
function filter_admin_overview_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for filter_admin_overview().
```

## Code

```php
function filter_admin_overview_submit($form, &$form_state) {
  foreach ($form_state['values']['formats'] as $id => $data) {
    if (is_array($data) && isset($data['weight'])) {
      // Only update if this is a form element with weight.
      db_update('filter_format')
        ->fields(array('weight' => $data['weight']))
        ->condition('format', $id)
        ->execute();
    }
  }
  filter_formats_reset();
  drupal_set_message(t('The text format ordering has been saved.'));
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
