# CommonURLUnitTest::testLXSS()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 88–114 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L88-L114)
- **Class:** [CommonURLUnitTest](../CommonURLUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testLXSS()
```

## Documentation

```text
Confirm that invalid text given as $path is filtered.
```

## Code

```php
  function testLXSS() {
    $text = $this->randomName();
    $path = "<SCRIPT>alert('XSS')</SCRIPT>";
    $link = l($text, $path);
    $sanitized_path = check_url(url($path));
    $this->assertTrue(strpos($link, $sanitized_path) !== FALSE, format_string('XSS attack @path was filtered', array('@path' => $path)));

    // Verify that a dangerous protocol is sanitized.
    $text = $this->randomName();
    $path = "javascript:alert('XSS')";
    $link = l($text, $path, array('external' => TRUE));
    $this->assertTrue(strpos($link, 'javascript:') === FALSE, 'Dangerous protocol javascript: was sanitized.');

    // Verify that these harmless javascript paths are left intact for BC.
    $special_case_js_paths = array(
      'javascript:void()',
      'javascript:void();',
      'javascript:void(0)',
      'javascript:void(0);',
      'JavaScript:Void(0)'
    );
    foreach ($special_case_js_paths as $path) {
      $text = $this->randomName();
      $link = l($text, $path, array('external' => TRUE));
      $this->assertTrue(strpos($link, $path) !== FALSE, format_string('Harmless @path was not sanitized.', array('@path' => $path)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
