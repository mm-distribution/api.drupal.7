# Stub::fromContent()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Stub.php`](../_file.md), lines 23–38 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Stub.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Stub.php#L23-L38)
- **Class:** [Stub](../Stub.md)

## Signature

```php
public static function fromContent($content)
```

## Documentation

```text
@param string $content
@return self
```

## Code

```php
    public static function fromContent($content)
    {
        $target = new static();
        $target->content = $content;

        if (
            stripos($content, 'Phar::mapPhar(') !== false
            && preg_match('#Phar\:\:mapPhar\(([^)]+)\)#', $content, $matches)
        ) {
            // remove spaces, single & double quotes
            // @todo `'my' . 'alias' . '.phar'` is not evaluated here
            $target->mappedAlias = trim($matches[1], ' \'"');
        }

        return $target;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Stub.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Stub.php) · Licensed GPL-2.0-or-later (see LICENSE)._
