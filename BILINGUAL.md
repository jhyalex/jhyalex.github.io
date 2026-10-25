# Bilingual edition

Chinese remains the source text. The 28 original `_posts` files are unchanged.
English translations are stored as Markdown strings in `_data/en/*.json`.
`_data/translation_keys.json` maps each original source path to its translation;
this intentionally does not use the article date alone, because dates are not unique.

## Reading

- Chinese URLs remain unchanged.
- English home: `/en/`; article routes: `/en/posts/<translation-key>/`.
- Header and article language links connect corresponding pages.
- All text is rendered by Jekyll. Reading and switching languages work without JavaScript.
- JavaScript only remembers an explicit language choice and redirects subsequent visits
  to the root homepage when English was selected. Internal navigation stays in its locale.
- Home listings, About, tags, navigation, previous/next links, error/offline pages,
  RSS, page metadata, and the web-app manifest have English versions.
- The English archive currently has three pages of ten posts, matching the 28-post source.

## Translation policy

Preserve meaning, imagery, key vocabulary, uncertainty, repetition, and paragraph/verse
structure. Adjust word order and sentence construction for English. Do not rewrite
Chinese originals, complete unfinished stories, silently correct claims, or invent
sources for private references. Existing English passages and code examples are retained.
Notes are explicitly labeled and separate from the author's text. The Markdown tutorial
retains Riku's attribution and all credits and examples.

The author specifically confirmed **loafing**, referring to Larry in Maugham's
*The Razor's Edge*, for 甩膀子 in *A Night at the Greek Theatre*.
Hailuo is a transliteration of 海螺, treated provisionally as a personal name.
The unattributed old-book quotation in that essay is translated without assigning a source.
The Yellowstone placeholders and unfinished stories remain unfinished.
The historical facts and advice in old essays are translated, not editorially updated.
The fictional Aria Morta appendix has a brief note distinguishing perfume from an edible ingredient.

## Adding or editing an article

1. Keep the Chinese post in `_posts/` as usual.
2. Add/update the English `title`, `subtitle`, and full Markdown `body` in `_data/en/`.
3. Map the exact source path in `_data/translation_keys.json`.
4. Add the small English page descriptor in `en/posts/`, copying the original image
   and catalog setting. Set `source_path`, `lang: en`, and a unique English permalink.
5. Add any new tag to `_data/tags_en.json`.
6. If the total exceeds 30, add another English archive page and update the pager.
7. Run `jekyll build`, then `python3 scripts/check_bilingual.py _site`.

## Reference checks for translator notes

- Larry's loafing: https://www.litcharts.com/lit/the-razor-s-edge/part-2-chapter-2
- Chinese/English title of 正见: https://khyentsefoundation.org/chs/resource/book_movie/what-makes-you-not-a-buddhist/
- Jiang Kui, 暗香: https://www.shidianguji.com/book/SBCK231/chapter/1j741jxm5v6lh_183
- Xu Zhimo, 再别康桥: https://zh.wikisource.org/zh-hans/再别康桥
- Zheng Chouyu, 错误: https://www.chinawriter.com.cn/n1/2025/0616/c404063-40501149.html
- Wang Bo's opening couplet on About: https://m.guwendao.net/mingju/juv_6578d3ae8312.aspx
- Repeated sunsets in The Little Prince: https://www.b612.cn/read/06.html
  (The poem's own number, 42, is preserved.)

An initially suspected Tagore reference was not assigned to a specific book because its
source could not be established confidently. The verse itself is translated unchanged.
