# Reader::extractData()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](../_file.md), lines 87–138 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L87-L138)
- **Class:** [Reader](../Reader.md)

## Signature

```php
private function extractData($fileName)
```

## Documentation

```text
@param string $fileName e.g. '/path/file.phar' or 'compress.zlib:///path/file.phar'
@return array
```

## Code

```php
    private function extractData($fileName)
    {
        $stubContent = null;
        $manifestContent = null;
        $manifestLength = null;

        $resource = fopen($fileName, 'r');
        if (!is_resource($resource)) {
            throw new ReaderException(
                sprintf('Resource %s could not be opened', $fileName),
                1547902055
            );
        }

        while (!feof($resource)) {
            $line = fgets($resource);
            // stop reading file when manifest can be extracted
            if ($manifestLength !== null && $manifestContent !== null && strlen($manifestContent) >= $manifestLength) {
                break;
            }

            $manifestPosition = strpos($line, '__HALT_COMPILER();');

            // first line contains start of manifest
            if ($stubContent === null && $manifestContent === null && $manifestPosition !== false) {
                $stubContent = substr($line, 0, $manifestPosition - 1);
                $manifestContent = preg_replace('#^.*__HALT_COMPILER\(\);(?>[ \n]\?>(?>\r\n|\n)?)?#', '', $line);
                $manifestLength = $this->resolveManifestLength($manifestContent);
            // line contains start of stub
            } elseif ($stubContent === null) {
                $stubContent = $line;
            // line contains start of manifest
            } elseif ($manifestContent === null && $manifestPosition !== false) {
                $manifestContent = preg_replace('#^.*__HALT_COMPILER\(\);(?>[ \n]\?>(?>\r\n|\n)?)?#', '', $line);
                $manifestLength = $this->resolveManifestLength($manifestContent);
            // manifest has been started (thus is cannot be stub anymore), add content
            } elseif ($manifestContent !== null) {
                $manifestContent .= $line;
                $manifestLength = $this->resolveManifestLength($manifestContent);
            // stub has been started (thus cannot be manifest here, yet), add content
            } elseif ($stubContent !== null) {
                $stubContent .= $line;
            }
        }
        fclose($resource);

        return array(
            'stubContent' => $stubContent,
            'manifestContent' => $manifestContent,
            'manifestLength' => $manifestLength,
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
