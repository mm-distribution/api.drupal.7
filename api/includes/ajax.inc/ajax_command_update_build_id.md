# ajax_command_update_build_id()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1289–1295 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1289-L1295)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_update_build_id($form)
```

## Documentation

```text
Creates a Drupal Ajax 'update_build_id' command.

This command updates the value of a hidden form_build_id input element on a
form. It requires the form passed in to have keys for both the old build ID
in #build_id_old and the new build ID in #build_id.

The primary use case for this Ajax command is to serve a new build ID to a
form served from the cache to an anonymous user, preventing one anonymous
user from accessing the form state of another anonymous users on Ajax enabled
forms.

@param $form
  The form array representing the form whose build ID should be updated.
```

## Code

```php
function ajax_command_update_build_id($form) {
  return array(
    'command' => 'updateBuildId',
    'old' => $form['#build_id_old'],
    'new' => $form['#build_id'],
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
