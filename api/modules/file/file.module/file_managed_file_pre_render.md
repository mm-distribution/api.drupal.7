# file_managed_file_pre_render()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 773–784 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L773-L784)
- **Module/theme:** file

## Signature

```php
function file_managed_file_pre_render($element)
```

## Documentation

```text
#pre_render callback to hide display of the upload or remove controls.

Upload controls are hidden when a file is already uploaded. Remove controls
are hidden when there is no file attached. Controls are hidden here instead
of in file_managed_file_process(), because #access for these buttons depends
on the managed_file element's #value. See the documentation of form_builder()
for more detailed information about the relationship between #process,
#value, and #access.

Because #access is set here, it affects display only and does not prevent
JavaScript or other untrusted code from submitting the form as though access
were enabled. The form processing functions for these elements should not
assume that the buttons can't be "clicked" just because they are not
displayed.

@see file_managed_file_process()
@see form_builder()
```

## Code

```php
function file_managed_file_pre_render($element) {
  // If we already have a file, we don't want to show the upload controls.
  if (!empty($element['#value']['fid'])) {
    $element['upload']['#access'] = FALSE;
    $element['upload_button']['#access'] = FALSE;
  }
  // If we don't already have a file, there is nothing to remove.
  else {
    $element['remove_button']['#access'] = FALSE;
  }
  return $element;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
