# DBLogTestCase::getContent()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 414–433 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L414-L433)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function getContent($type)
```

## Documentation

```text
Creates random content based on node content type.

@param string $type
  Node content type (e.g., 'article').

@return array
  Random content needed by various node types.
```

## Code

```php
  private function getContent($type) {
    $langcode = LANGUAGE_NONE;
    switch ($type) {
      case 'poll':
        $content = array(
          "title" => $this->randomName(8),
          'choice[new:0][chtext]' => $this->randomName(32),
          'choice[new:1][chtext]' => $this->randomName(32),
        );
      break;

      default:
        $content = array(
          "title" => $this->randomName(8),
          "body[$langcode][0][value]" => $this->randomName(32),
        );
      break;
    }
    return $content;
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
