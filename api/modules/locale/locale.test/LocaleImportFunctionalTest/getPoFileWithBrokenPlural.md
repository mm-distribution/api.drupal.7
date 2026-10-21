# LocaleImportFunctionalTest::getPoFileWithBrokenPlural()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1331–1344 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1331-L1344)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function getPoFileWithBrokenPlural()
```

## Documentation

```text
Returns a .po file with a broken plural formula.
```

## Code

```php
  function getPoFileWithBrokenPlural() {
    return <<< EOF
msgid ""
msgstr ""
"Project-Id-Version: Drupal 7\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: broken, will not parse\\n"

msgid "Monday"
msgstr "lundi"
EOF;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
