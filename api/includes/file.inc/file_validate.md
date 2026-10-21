# file_validate()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1745–1768 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1745-L1768)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_validate(stdClass &$file, $validators = array())
```

## Documentation

```text
Checks that a file meets the criteria specified by the validators.

After executing the validator callbacks specified hook_file_validate() will
also be called to allow other modules to report errors about the file.

@param $file
  A Drupal file object.
@param $validators
  An optional, associative array of callback functions used to validate the
  file. The keys are function names and the values arrays of callback
  parameters which will be passed in after the file object. The
  functions should return an array of error messages; an empty array
  indicates that the file passed validation. The functions will be called in
  the order specified.

@return
  An array containing validation error messages.

@see hook_file_validate()
```

## Code

```php
function file_validate(stdClass &$file, $validators = array()) {
  // Call the validation functions specified by this function's caller.
  $errors = array();
  foreach ($validators as $function => $args) {
    if (function_exists($function)) {
      array_unshift($args, $file);
      $errors = array_merge($errors, call_user_func_array($function, $args));
    }
  }

  // Let other modules perform validation on the new file.
  $errors = array_merge($errors, module_invoke_all('file_validate', $file));

  // Ensure the file does not contain a malicious extension. At this point
  // file_save_upload() will have munged the file so it does not contain a
  // malicious extension. Contributed and custom code that calls this method
  // needs to take similar steps if they need to permit files with malicious
  // extensions to be uploaded.
  if (empty($errors) && !variable_get('allow_insecure_uploads', 0) && preg_match('/\.(' . FILE_INSECURE_EXTENSIONS . ')(\.|$)/i', $file->filename)) {
    $errors[] = t('For security reasons, your upload has been rejected.');
  }

  return $errors;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
