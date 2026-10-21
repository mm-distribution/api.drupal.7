# Reader::resolveManifestLength()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](../_file.md), lines 197–203 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L197-L203)
- **Class:** [Reader](../Reader.md)

## Signature

```php
private function resolveManifestLength($content)
```

## Documentation

```text
@param string $content
@return int|null
```

## Code

```php
    private function resolveManifestLength($content)
    {
        if (strlen($content) < 4) {
            return null;
        }
        return static::resolveFourByteLittleEndian($content, 0);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
