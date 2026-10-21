# ajax_command_settings()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1181–1187 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1181-L1187)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_settings($argument, $merge = FALSE)
```

## Documentation

```text
Creates a Drupal Ajax 'settings' command.

The 'settings' command instructs the client either to use the given array as
the settings for ajax-loaded content or to extend Drupal.settings with the
given array, depending on the value of the $merge parameter.

This command is implemented by Drupal.ajax.prototype.commands.settings()
defined in misc/ajax.js.

@param $argument
  An array of key/value pairs to add to the settings. This will be utilized
  for all commands after this if they do not include their own settings
  array.
@param $merge
  Whether or not the passed settings in $argument should be merged into the
  global Drupal.settings on the page. By default (FALSE), the settings that
  are passed to Drupal.attachBehaviors will not include the global
  Drupal.settings.

@return
  An array suitable for use with the ajax_render() function.
```

## Code

```php
function ajax_command_settings($argument, $merge = FALSE) {
  return array(
    'command' => 'settings',
    'settings' => $argument,
    'merge' => $merge,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
