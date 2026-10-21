# DrupalHtmlToTextTestCase::testDrupalHtmlToTextBlockTagToNewline()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 389–434 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L389-L434)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalHtmlToTextBlockTagToNewline()
```

## Documentation

```text
Test that text separated by block-level tags in HTML get separated by
(at least) a newline in the plaintext version.
```

## Code

```php
  function testDrupalHtmlToTextBlockTagToNewline() {
    $input = '[text]'
      . '<blockquote>[blockquote]</blockquote>'
      . '<br />[br]'
      . '<dl><dt>[dl-dt]</dt>'
      . '<dt>[dt]</dt>'
      . '<dd>[dd]</dd>'
      . '<dd>[dd-dl]</dd></dl>'
      . '<h1>[h1]</h1>'
      . '<h2>[h2]</h2>'
      . '<h3>[h3]</h3>'
      . '<h4>[h4]</h4>'
      . '<h5>[h5]</h5>'
      . '<h6>[h6]</h6>'
      . '<hr />[hr]'
      . '<ol><li>[ol-li]</li>'
      . '<li>[li]</li>'
      . '<li>[li-ol]</li></ol>'
      . '<p>[p]</p>'
      . '<ul><li>[ul-li]</li>'
      . '<li>[li-ul]</li></ul>'
      . '[text]';
    $output = drupal_html_to_text($input);
    $pass = $this->assertFalse(
      preg_match('/\][^\n]*\[/s', $output),
      'Block-level HTML tags should force newlines'
    );
    if (!$pass) {
      $this->verbose($this->stringToHtml($output));
    }
    $output_upper = drupal_strtoupper($output);
    $upper_input = drupal_strtoupper($input);
    $upper_output = drupal_html_to_text($upper_input);
    $pass = $this->assertEqual(
      $upper_output,
      $output_upper,
      'Tag recognition should be case-insensitive'
    );
    if (!$pass) {
      $this->verbose(
        $upper_output
        . '<br />should  be equal to <br />'
        . $output_upper
      );
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
