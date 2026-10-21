# poll_form()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 235–355 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L235-L355)
- **Module/theme:** poll
- **Implements:** [hook_form()](../../node/node.api.php/hook_form.md)

## Signature

```php
function poll_form($node, &$form_state)
```

## Documentation

```text
Implements hook_form().
```

## Code

```php
function poll_form($node, &$form_state) {
  global $user;

  $admin = user_access('bypass node access') || user_access('edit any poll content') || (user_access('edit own poll content') && $user->uid == $node->uid);

  $type = node_type_get_type($node);

  // The submit handlers to add more poll choices require that this form is
  // cached, regardless of whether Ajax is used.
  $form_state['cache'] = TRUE;

  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => check_plain($type->title_label),
    '#required' => TRUE,
    '#default_value' => $node->title,
    '#maxlength' => 255,
    '#weight' => -5,
  );

  if (isset($form_state['choice_count'])) {
    $choice_count = $form_state['choice_count'];
  }
  else {
    $choice_count = max(2, empty($node->choice) ? 2 : count($node->choice));
  }

  // Add a wrapper for the choices and more button.
  $form['choice_wrapper'] = array(
    '#tree' => FALSE,
    '#weight' => -4,
    '#prefix' => '<div class="clearfix" id="poll-choice-wrapper">',
    '#suffix' => '</div>',
  );

  // Container for just the poll choices.
  $form['choice_wrapper']['choice'] = array(
    '#prefix' => '<div id="poll-choices">',
    '#suffix' => '</div>',
    '#theme' => 'poll_choices',
  );

  // Add the current choices to the form.
  $delta = 0;
  $weight = 0;
  if (isset($node->choice)) {
    $delta = count($node->choice);
    foreach ($node->choice as $chid => $choice) {
      $key = 'chid:' . $chid;
      $form['choice_wrapper']['choice'][$key] = _poll_choice_form($key, $choice['chid'], $choice['chtext'], $choice['chvotes'], $choice['weight'], $choice_count);
      $weight = max($choice['weight'], $weight);
    }
  }

  // Add initial or additional choices.
  $existing_delta = $delta;
  for ($delta; $delta < $choice_count; $delta++) {
    $key = 'new:' . ($delta - $existing_delta);
    // Increase the weight of each new choice.
    $weight++;
    $form['choice_wrapper']['choice'][$key] = _poll_choice_form($key, NULL, '', 0, $weight, $choice_count);
  }

  // We name our button 'poll_more' to avoid conflicts with other modules using
  // Ajax-enabled buttons with the id 'more'.
  $form['choice_wrapper']['poll_more'] = array(
    '#type' => 'submit',
    '#value' => t('More choices'),
    '#attributes' => array(
      'title' => t("If the amount of boxes above isn't enough, click here to add more choices."),
    ),
    '#weight' => 1,
    '#limit_validation_errors' => array(array('choice')),
    '#submit' => array('poll_more_choices_submit'),
    '#ajax' => array(
      'callback' => 'poll_choice_js',
      'wrapper' => 'poll-choices',
      'effect' => 'fade',
    ),
  );

  // Poll attributes
  $duration = array(
    // 1-6 days.
    86400, 2 * 86400, 3 * 86400, 4 * 86400, 5 * 86400, 6 * 86400,
    // 1-3 weeks (7 days).
    604800, 2 * 604800, 3 * 604800,
    // 1-3,6,9 months (30 days).
    2592000, 2 * 2592000, 3 * 2592000, 6 * 2592000, 9 * 2592000,
    // 1 year (365 days).
    31536000,
  );
  $duration = array(0 => t('Unlimited')) + drupal_map_assoc($duration, 'format_interval');
  $active = array(0 => t('Closed'), 1 => t('Active'));

  $form['settings'] = array(
    '#type' => 'fieldset',
    '#collapsible' => TRUE,
    '#title' => t('Poll settings'),
    '#weight' => -3,
    '#access' => $admin,
  );

  $form['settings']['active'] = array(
    '#type' => 'radios',
    '#title' => t('Poll status'),
    '#default_value' => isset($node->active) ? $node->active : 1,
    '#options' => $active,
    '#description' => t('When a poll is closed, visitors can no longer vote for it.'),
    '#access' => $admin,
  );
  $form['settings']['runtime'] = array(
    '#type' => 'select',
    '#title' => t('Poll duration'),
    '#default_value' => isset($node->runtime) ? $node->runtime : 0,
    '#options' => $duration,
    '#description' => t('After this period, the poll will be closed automatically.'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
