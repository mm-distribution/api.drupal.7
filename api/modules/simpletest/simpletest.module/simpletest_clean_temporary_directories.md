# simpletest_clean_temporary_directories()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 589–609 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L589-L609)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_clean_temporary_directories()
```

## Documentation

```text
Find all leftover temporary directories and remove them.
```

## Code

```php
function simpletest_clean_temporary_directories() {
  $count = 0;
  if (is_dir('public://simpletest')) {
    $files = scandir('public://simpletest');
    foreach ($files as $file) {
      $path = 'public://simpletest/' . $file;
      // Ensure that cache directories are cleaned as well.
      if (is_dir($path) && (is_numeric($file) || strpos($file, '1c') === 0)) {
        file_unmanaged_delete_recursive($path);
        $count++;
      }
    }
  }

  if ($count > 0) {
    drupal_set_message(format_plural($count, 'Removed 1 temporary directory.', 'Removed @count temporary directories.'));
  }
  else {
    drupal_set_message(t('No temporary directories to remove.'));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
