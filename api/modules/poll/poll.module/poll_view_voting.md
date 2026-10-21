# poll_view_voting()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 707–738 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L707-L738)
- **Module/theme:** poll
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function poll_view_voting($form, &$form_state, $node, $block = FALSE)
```

## Documentation

```text
Generates the voting form for a poll.

@ingroup forms
@see poll_vote()
@see phptemplate_preprocess_poll_vote()
```

## Code

```php
function poll_view_voting($form, &$form_state, $node, $block = FALSE) {
  if ($node->choice) {
    $list = array();
    foreach ($node->choice as $i => $choice) {
      $list[$i] = check_plain($choice['chtext']);
    }
    $form['choice'] = array(
      '#type' => 'radios',
      '#title' => t('Choices'),
      '#title_display' => 'invisible',
      '#options' => $list,
    );
  }

  $form['vote'] = array(
    '#type' => 'submit',
    '#value' => t('Vote'),
    '#submit' => array('poll_vote'),
  );

  // Store the node so we can get to it in submit functions.
  $form['#node'] = $node;
  $form['#block'] = $block;

  // Set form caching because we could have multiple of these forms on
  // the same page, and we want to ensure the right one gets picked.
  $form_state['cache'] = TRUE;

  // Provide a more cleanly named voting form theme.
  $form['#theme'] = 'poll_vote';
  return $form;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
