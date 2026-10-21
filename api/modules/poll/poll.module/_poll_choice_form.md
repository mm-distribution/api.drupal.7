# _poll_choice_form()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 381–425 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L381-L425)
- **Module/theme:** poll

## Signature

```php
function _poll_choice_form($key, $chid = NULL, $value = '', $votes = 0, $weight = 0, $size = 10)
```

## Documentation

_No docblock in source._

## Code

```php
function _poll_choice_form($key, $chid = NULL, $value = '', $votes = 0, $weight = 0, $size = 10) {
  $form = array(
    '#tree' => TRUE,
    '#weight' => $weight,
  );

  // We'll manually set the #parents property of these fields so that
  // their values appear in the $form_state['values']['choice'] array.
  $form['chid'] = array(
    '#type' => 'value',
    '#value' => $chid,
    '#parents' => array('choice', $key, 'chid'),
  );

  $form['chtext'] = array(
    '#type' => 'textfield',
    '#title' => $value !== '' ? t('Choice label') : t('New choice label'),
    '#title_display' => 'invisible',
    '#default_value' => $value,
    '#parents' => array('choice', $key, 'chtext'),
  );

  $form['chvotes'] = array(
    '#type' => 'textfield',
    '#title' => $value !== '' ? t('Vote count for choice @label', array('@label' => $value)) : t('Vote count for new choice'),
    '#title_display' => 'invisible',
    '#default_value' => $votes,
    '#size' => 5,
    '#maxlength' => 7,
    '#parents' => array('choice', $key, 'chvotes'),
    '#access' => user_access('administer nodes'),
    '#element_validate' => array('element_validate_integer'),
  );

  $form['weight'] = array(
    '#type' => 'weight',
    '#title' => $value !== '' ? t('Weight for choice @label', array('@label' => $value)) : t('Weight for new choice'),
    '#title_display' => 'invisible',
    '#default_value' => $weight,
    '#delta' => $size,
    '#parents' => array('choice', $key, 'weight'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
