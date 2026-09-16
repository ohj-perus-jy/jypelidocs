-- Sisennetty koodilohko (ei luokkia) -> aita tunnisteella, jotta tim2md.py
-- voi antaa sille kielen kuten aidoille.
function CodeBlock(el)
  if #el.classes == 0 then
    el.classes = {"timindented"}
  end
  return el
end
