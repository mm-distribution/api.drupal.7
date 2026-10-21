# poll_field_extra_fields()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 201–230 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L201-L230)
- **Module/theme:** poll
- **Implements:** [hook_field_extra_fields()](../../field/field.api.php/hook_field_extra_fields.md)

## Signature

```php
function poll_field_extra_fields()
```

## Documentation

```text
Implements hook_field_extra_fields().
```

## Code

```php
function poll_field_extra_fields() {
  $extra['node']['poll'] = array(
    'form' => array(
      'choice_wrapper' => array(
        'label' => t('Poll choices'),
        'description' => t('Poll choices'),
        'weight' => -4,
      ),
      'settings' => array(
        'label' => t('Poll settings'),
        'description' => t('Poll module settings'),
        'weight' => -3,
      ),
    ),
    'display' => array(
      'poll_view_voting' => array(
        'label' => t('Poll vote'),
        'description' => t('Poll vote'),
        'weight' => 0,
      ),
      'poll_view_results' => array(
        'label' => t('Poll results'),
        'description' => t('Poll results'),
        'weight' => 0,
      ),
    )
  );

  return $extra;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
