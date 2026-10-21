# InfoFileParserTestCase::testDrupalParseInfoFormat()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2378–2434 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2378-L2434)
- **Class:** [InfoFileParserTestCase](../InfoFileParserTestCase.md)
- **Module/theme:** system

## Signature

```php
function testDrupalParseInfoFormat()
```

## Documentation

```text
Test drupal_parse_info_format().
```

## Code

```php
  function testDrupalParseInfoFormat() {
    $config = '
simple = Value
quoted = " Value"
multiline = "Value
  Value"
array[] = Value1
array[] = Value2
array_assoc[a] = Value1
array_assoc[b] = Value2
array_deep[][][] = Value
array_deep_assoc[a][b][c] = Value
array_space[a b] = Value';

    $expected = array(
      'simple' => 'Value',
      'quoted' => ' Value',
      'multiline' => "Value\n  Value",
      'array' => array(
        0 => 'Value1',
        1 => 'Value2',
      ),
      'array_assoc' => array(
        'a' => 'Value1',
        'b' => 'Value2',
      ),
      'array_deep' => array(
        0 => array(
          0 => array(
            0 => 'Value',
          ),
        ),
      ),
      'array_deep_assoc' => array(
        'a' => array(
          'b' => array(
            'c' => 'Value',
          ),
        ),
      ),
      'array_space' => array(
        'a b' => 'Value',
      ),
    );

    $parsed = drupal_parse_info_format($config);

    $this->assertEqual($parsed['simple'], $expected['simple'], 'Set a simple value.');
    $this->assertEqual($parsed['quoted'], $expected['quoted'], 'Set a simple value in quotes.');
    $this->assertEqual($parsed['multiline'], $expected['multiline'], 'Set a multiline value.');
    $this->assertEqual($parsed['array'], $expected['array'], 'Set a simple array.');
    $this->assertEqual($parsed['array_assoc'], $expected['array_assoc'], 'Set an associative array.');
    $this->assertEqual($parsed['array_deep'], $expected['array_deep'], 'Set a nested array.');
    $this->assertEqual($parsed['array_deep_assoc'], $expected['array_deep_assoc'], 'Set a nested associative array.');
    $this->assertEqual($parsed['array_space'], $expected['array_space'], 'Set an array with a whitespace in the key.');
    $this->assertEqual($parsed, $expected, 'Entire parsed .info string and expected array are identical.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
