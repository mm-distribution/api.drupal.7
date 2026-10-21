# theme_poll_choices()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 844–887 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L844-L887)
- **Module/theme:** poll
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_poll_choices($variables)
```

## Documentation

```text
Returns HTML for an admin poll form for choices.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_poll_choices($variables) {
  $form = $variables['form'];

  drupal_add_tabledrag('poll-choice-table', 'order', 'sibling', 'poll-weight');

  $is_admin= user_access('administer nodes');
  $delta = 0;
  $rows = array();
  $headers = array('', t('Choice'));
  if ($is_admin) {
    $headers[] = t('Vote count');
  }
  $headers[] = t('Weight');

  foreach (element_children($form) as $key) {
    $delta++;
    // Set special classes for drag and drop updating.
    $form[$key]['weight']['#attributes']['class'] = array('poll-weight');

    // Build the table row.
    $row = array(
      'data' => array(
        array('class' => array('choice-flag')),
        drupal_render($form[$key]['chtext']),
      ),
      'class' => array('draggable'),
    );
    if ($is_admin) {
      $row['data'][] = drupal_render($form[$key]['chvotes']);
    }
    $row['data'][] = drupal_render($form[$key]['weight']);

    // Add any additional classes set on the row.
    if (!empty($form[$key]['#attributes']['class'])) {
      $row['class'] = array_merge($row['class'], $form[$key]['#attributes']['class']);
    }

    $rows[] = $row;
  }

  $output = theme('table', array('header' => $headers, 'rows' => $rows, 'attributes' => array('id' => 'poll-choice-table')));
  $output .= drupal_render_children($form);
  return $output;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
