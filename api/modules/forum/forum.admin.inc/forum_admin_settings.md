# forum_admin_settings()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 236–259 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L236-L259)
- **Module/theme:** forum
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function forum_admin_settings($form)
```

## Documentation

```text
Form constructor for the forum settings page.

@see forum_menu()
@see system_settings_form()
@ingroup forms
```

## Code

```php
function forum_admin_settings($form) {
  $number = drupal_map_assoc(array(5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 80, 100, 150, 200, 250, 300, 350, 400, 500));
  $form['forum_hot_topic'] = array('#type' => 'select',
    '#title' => t('Hot topic threshold'),
    '#default_value' => variable_get('forum_hot_topic', 15),
    '#options' => $number,
    '#description' => t('The number of replies a topic must have to be considered "hot".'),
  );
  $number = drupal_map_assoc(array(10, 25, 50, 75, 100));
  $form['forum_per_page'] = array('#type' => 'select',
    '#title' => t('Topics per page'),
    '#default_value' => variable_get('forum_per_page', 25),
    '#options' => $number,
    '#description' => t('Default number of forum topics displayed per page.'),
  );
  $forder = array(1 => t('Date - newest first'), 2 => t('Date - oldest first'), 3 => t('Posts - most active first'), 4 => t('Posts - least active first'));
  $form['forum_order'] = array('#type' => 'radios',
    '#title' => t('Default order'),
    '#default_value' => variable_get('forum_order', 1),
    '#options' => $forder,
    '#description' => t('Default display order for topics.'),
  );
  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
