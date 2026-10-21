# CascadingStylesheetsUnitTest::testLoadCssBasic()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1113–1147 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1113-L1147)
- **Class:** [CascadingStylesheetsUnitTest](../CascadingStylesheetsUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testLoadCssBasic()
```

## Documentation

```text
Tests basic CSS loading with and without optimization via drupal_load_stylesheet().

Known tests:
- Retain white-space in selectors. (https://drupal.org/node/472820)
- Proper URLs in imported files. (https://drupal.org/node/265719)
- Retain pseudo-selectors. (https://drupal.org/node/460448)
- Don't adjust data URIs. (https://drupal.org/node/2142441)
- Files imported from external URLs. (https://drupal.org/node/2014851)
```

## Code

```php
  function testLoadCssBasic() {
    // Array of files to test living in 'simpletest/files/css_test_files/'.
    // - Original: name.css
    // - Unoptimized expected content: name.css.unoptimized.css
    // - Optimized expected content: name.css.optimized.css
    $testfiles = array(
      'css_input_without_import.css',
      'css_input_with_import.css',
      'css_subfolder/css_input_with_import.css',
      'comment_hacks.css',
      'quotes.css',
    );
    $path = drupal_get_path('module', 'simpletest') . '/files/css_test_files';
    foreach ($testfiles as $file) {
      $file_path = $path . '/' . $file;
      $file_url = $GLOBALS['base_url'] . '/' . $file_path;

      $expected = file_get_contents($file_path . '.unoptimized.css');
      $unoptimized_output = drupal_load_stylesheet($file_path, FALSE);
      $this->assertEqual($unoptimized_output, $expected, format_string('Unoptimized CSS file has expected contents (@file)', array('@file' => $file)));

      $expected = file_get_contents($file_path . '.optimized.css');
      $optimized_output = drupal_load_stylesheet($file_path, TRUE);
      $this->assertEqual($optimized_output, $expected, format_string('Optimized CSS file has expected contents (@file)', array('@file' => $file)));

      // Repeat the tests by accessing the stylesheets by URL.
      $expected = file_get_contents($file_path . '.unoptimized.css');
      $unoptimized_output_url = drupal_load_stylesheet($file_url, FALSE);
      $this->assertEqual($unoptimized_output_url, $expected, format_string('Unoptimized CSS file (loaded from an URL) has expected contents (@file)', array('@file' => $file)));

      $expected = file_get_contents($file_path . '.optimized.css');
      $optimized_output_url = drupal_load_stylesheet($file_url, TRUE);
      $this->assertEqual($optimized_output_url, $expected, format_string('Optimized CSS file (loaded from an URL) has expected contents (@file)', array('@file' => $file)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
