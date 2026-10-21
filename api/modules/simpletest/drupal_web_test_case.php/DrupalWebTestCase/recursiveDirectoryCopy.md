# DrupalWebTestCase::recursiveDirectoryCopy()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1663–1680 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1663-L1680)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function recursiveDirectoryCopy($src, $dst)
```

## Documentation

```text
Recursively copy one directory to another.

@param $src
  The source directory.
@param $dest
  The destination directory.
```

## Code

```php
  protected function recursiveDirectoryCopy($src, $dst) {
    $dir = opendir($src);

    if (!file_exists($dst)){
      mkdir($dst);
    }
    while (($file = readdir($dir)) !== FALSE) {
      if ($file != '.' && $file != '..') {
        if (is_dir($src . '/' . $file)) {
          $this->recursiveDirectoryCopy($src . '/' . $file, $dst . '/' . $file);
        }
        else {
          copy($src . '/' . $file, $dst . '/' . $file);
        }
      }
    }
    closedir($dir);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
