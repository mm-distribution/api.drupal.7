# TokenReplaceTestCase::testSystemDateTokenReplacement()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2341–2363 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2341-L2363)
- **Class:** [TokenReplaceTestCase](../TokenReplaceTestCase.md)
- **Module/theme:** system

## Signature

```php
function testSystemDateTokenReplacement()
```

## Documentation

```text
Tests the generation of all system date tokens.
```

## Code

```php
  function testSystemDateTokenReplacement() {
    global $language;

    // Set time to one hour before request.
    $date = REQUEST_TIME - 3600;

    // Generate and test tokens.
    $tests = array();
    $tests['[date:short]'] = format_date($date, 'short', '', NULL, $language->language);
    $tests['[date:medium]'] = format_date($date, 'medium', '', NULL, $language->language);
    $tests['[date:long]'] = format_date($date, 'long', '', NULL, $language->language);
    $tests['[date:custom:m/j/Y]'] = format_date($date, 'custom', 'm/j/Y', NULL, $language->language);
    $tests['[date:since]'] = format_interval((REQUEST_TIME - $date), 2, $language->language);
    $tests['[date:raw]'] = filter_xss($date);

    // Test to make sure that we generated something for each token.
    $this->assertFalse(in_array(0, array_map('strlen', $tests)), 'No empty tokens generated.');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('date' => $date), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Date token %token replaced.', array('%token' => $input)));
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
