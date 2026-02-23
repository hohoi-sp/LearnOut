export default function Home() {
  async function sendMessage(formData: FormData) {
    "use server";
    const body = JSON.stringify(Object.fromEntries(formData));
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/evaluate`, {
      method: "POST",
      body,
      headers: { "Content-Type": "application/json" },
    });
    if (!res.ok) throw new Error("Something went wrong");
    const data = await res.json();
    console.log(data);
  }

  return (
    <form action={sendMessage}>
      <input type="text" name="message" placeholder="メッセージを入力" />
      <button type="submit">送信</button>
    </form>
  );
}
