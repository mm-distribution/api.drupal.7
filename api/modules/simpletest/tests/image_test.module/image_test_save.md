# image_test_save()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 101–106 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L101-L106)
- **Module/theme:** batch_test

## Signature

```php
function image_test_save(stdClass $image, $destination)
```

## Documentation

```text
Image tookit's save operation.
```

## Code

```php
function image_test_save(stdClass $image, $destination) {
  _image_test_log_call('save', array($image, $destination));
  // Return false so that image_save() doesn't try to chmod the destination
  // file that we didn't bother to create.
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
