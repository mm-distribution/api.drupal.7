# comment_form_validate()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2138–2178 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2138-L2178)
- **Module/theme:** comment

## Signature

```php
function comment_form_validate($form, &$form_state)
```

## Documentation

```text
Validate comment form submissions.
```

## Code

```php
function comment_form_validate($form, &$form_state) {
  global $user;

  entity_form_field_validate('comment', $form, $form_state);

  if (!empty($form_state['values']['cid'])) {
    // Verify the name in case it is being changed from being anonymous.
    $account = user_load_by_name($form_state['values']['name']);
    $form_state['values']['uid'] = $account ? $account->uid : 0;

    if ($form_state['values']['date'] && strtotime($form_state['values']['date']) === FALSE) {
      form_set_error('date', t('You have to specify a valid date.'));
    }
    if ($form_state['values']['name'] && !$form_state['values']['is_anonymous'] && !$account) {
      form_set_error('name', t('You have to specify a valid author.'));
    }
  }
  elseif ($form_state['values']['is_anonymous']) {
    // Validate anonymous comment author fields (if given). If the (original)
    // author of this comment was an anonymous user, verify that no registered
    // user with this name exists.
    if ($form_state['values']['name']) {
      $query = db_select('users', 'u');
      $query->addField('u', 'uid', 'uid');
      $taken = $query
        ->condition('name', db_like($form_state['values']['name']), 'LIKE')
        ->countQuery()
        ->execute()
        ->fetchField();
      if ($taken) {
        form_set_error('name', t('The name you used belongs to a registered user.'));
      }
    }
  }
  if ($form_state['values']['mail'] && !valid_email_address($form_state['values']['mail'])) {
    form_set_error('mail', t('The e-mail address you specified is not valid.'));
  }
  if ($form_state['values']['homepage'] && !valid_url($form_state['values']['homepage'], TRUE)) {
    form_set_error('homepage', t('The URL of your homepage is not valid. Remember that it must be fully qualified, i.e. of the form <code>http://example.com/directory</code>.'));
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
