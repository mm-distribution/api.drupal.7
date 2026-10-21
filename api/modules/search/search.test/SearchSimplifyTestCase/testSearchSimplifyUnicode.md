# SearchSimplifyTestCase::testSearchSimplifyUnicode()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1150–1197 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1150-L1197)
- **Class:** [SearchSimplifyTestCase](../SearchSimplifyTestCase.md)
- **Module/theme:** search

## Signature

```php
function testSearchSimplifyUnicode()
```

## Documentation

```text
Tests that all Unicode characters simplify correctly.
```

## Code

```php
  function testSearchSimplifyUnicode() {
    // This test uses a file that was constructed so that the even lines are
    // boundary characters, and the odd lines are valid word characters. (It
    // was generated as a sequence of all the Unicode characters, and then the
    // boundary chararacters (punctuation, spaces, etc.) were split off into
    // their own lines).  So the even-numbered lines should simplify to nothing,
    // and the odd-numbered lines we need to split into shorter chunks and
    // verify that simplification doesn't lose any characters.
    $input = file_get_contents(DRUPAL_ROOT . '/modules/search/tests/UnicodeTest.txt');
    $basestrings = explode(chr(10), $input);
    $strings = array();
    foreach ($basestrings as $key => $string) {
      if ($key %2) {
        // Even line - should simplify down to a space.
        $simplified = search_simplify($string);
        $this->assertIdentical($simplified, ' ', "Line $key is excluded from the index");
      }
      else {
        // Odd line, should be word characters.
        // Split this into 30-character chunks, so we don't run into limits
        // of truncation in search_simplify().
        $start = 0;
        while ($start < drupal_strlen($string)) {
          $newstr = drupal_substr($string, $start, 30);
          // Special case: leading zeros are removed from numeric strings,
          // and there's one string in this file that is numbers starting with
          // zero, so prepend a 1 on that string.
          if (preg_match('/^[0-9]+$/', $newstr)) {
            $newstr = '1' . $newstr;
          }
          $strings[] = $newstr;
          $start += 30;
        }
      }
    }
    foreach ($strings as $key => $string) {
      $simplified = search_simplify($string);
      $this->assertTrue(drupal_strlen($simplified) >= drupal_strlen($string), "Nothing is removed from string $key.");
    }

    // Test the low-numbered ASCII control characters separately. They are not
    // in the text file because they are problematic for diff, especially \0.
    $string = '';
    for ($i = 0; $i < 32; $i++) {
      $string .= chr($i);
    }
    $this->assertIdentical(' ', search_simplify($string), 'Search simplify works for ASCII control characters.');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
