# TokenReplaceTestCase::testSystemTokenRecognition()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2271–2295 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2271-L2295)
- **Class:** [TokenReplaceTestCase](../TokenReplaceTestCase.md)
- **Module/theme:** system

## Signature

```php
function testSystemTokenRecognition()
```

## Documentation

```text
Test whether token-replacement works in various contexts.
```

## Code

```php
  function testSystemTokenRecognition() {
    global $language;

    // Generate prefixes and suffixes for the token context.
    $tests = array(
      array('prefix' => 'this is the ', 'suffix' => ' site'),
      array('prefix' => 'this is the', 'suffix' => 'site'),
      array('prefix' => '[', 'suffix' => ']'),
      array('prefix' => '', 'suffix' => ']]]'),
      array('prefix' => '[[[', 'suffix' => ''),
      array('prefix' => ':[:', 'suffix' => '--]'),
      array('prefix' => '-[-', 'suffix' => ':]:'),
      array('prefix' => '[:', 'suffix' => ']'),
      array('prefix' => '[site:', 'suffix' => ':name]'),
      array('prefix' => '[site:', 'suffix' => ']'),
    );

    // Check if the token is recognized in each of the contexts.
    foreach ($tests as $test) {
      $input = $test['prefix'] . '[site:name]' . $test['suffix'];
      $expected = $test['prefix'] . 'Drupal' . $test['suffix'];
      $output = token_replace($input, array(), array('language' => $language));
      $this->assertTrue($output == $expected, format_string('Token recognized in string %string', array('%string' => $input)));
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
