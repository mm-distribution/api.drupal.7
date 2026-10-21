# DBLogTestCase::getContentUpdate()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 444–461 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L444-L461)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function getContentUpdate($type)
```

## Documentation

```text
Creates random content as an update based on node content type.

@param string $type
  Node content type (e.g., 'article').

@return array
  Random content needed by various node types.
```

## Code

```php
  private function getContentUpdate($type) {
    switch ($type) {
      case 'poll':
        $content = array(
          'choice[chid:1][chtext]' => $this->randomName(32),
          'choice[chid:2][chtext]' => $this->randomName(32),
        );
      break;

      default:
        $langcode = LANGUAGE_NONE;
        $content = array(
          "body[$langcode][0][value]" => $this->randomName(32),
        );
      break;
    }
    return $content;
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
