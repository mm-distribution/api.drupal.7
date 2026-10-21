# CascadingStylesheetsTestCase::testRenderRemoveCharsetPreprocess()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 857–877 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L857-L877)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderRemoveCharsetPreprocess()
```

## Documentation

```text
Tests removing charset when rendering stylesheets with preprocessing on.
```

## Code

```php
  function testRenderRemoveCharsetPreprocess() {
    $cases = array(
      array(
        'asset' => '@charset "UTF-8";html{font-family:"sans-serif";}',
        'expected' => 'html{font-family:"sans-serif";}',
      ),
      // This asset contains extra \n character.
      array(
        'asset' => "@charset 'UTF-8';\nhtml{font-family:'sans-serif';}",
        'expected' => "\nhtml{font-family:'sans-serif';}",
      ),
    );

    foreach ($cases as $case) {
      $this->assertEqual(
        $case['expected'],
        drupal_load_stylesheet_content($case['asset']),
        'CSS optimizing correctly removes the charset declaration.'
      );
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
